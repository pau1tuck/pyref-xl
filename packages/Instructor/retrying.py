# Reference for retrying and validation features in Instructor using OpenAI and Tenacity

from typing import Annotated, Literal
from pydantic import BaseModel, Field, AfterValidator, field_validator
import openai
import instructor
from instructor.exceptions import InstructorRetryException
from tenacity import (
    Retrying,
    AsyncRetrying,
    stop_after_attempt,
    wait_fixed,
    wait_random,
    wait_exponential,
)

# Initialize the Instructor client
client = instructor.from_openai(openai.OpenAI(), mode=instructor.Mode.TOOLS)


# *** VALIDATION EXAMPLE ***
# Example 1: Basic Validator
def uppercase_validator(value: str):
    """
    Ensures the input string is in uppercase.
    """
    if value.islower():
        raise ValueError("Name must be ALL CAPS")
    return value


class UserDetail(BaseModel):
    """
    Represents a user with validation to ensure the name is uppercase.
    """

    name: Annotated[str, AfterValidator(uppercase_validator)]
    age: int


try:
    UserDetail(name="jason", age=12)
except Exception as e:
    print(e)
    """
    Output:
    1 validation error for UserDetail
    name
      Value error, Name must be ALL CAPS [type=value_error, input_value='jason', input_type=str]
    """


# *** SIMPLE RETRIES ***
class UserResponse(BaseModel):
    """
    A model for extracting user details with basic retry support.
    """

    name: str
    age: int


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=UserResponse,
    messages=[{"role": "user", "content": "Extract `jason is 12`"}],
    max_retries=3,  # Retries up to 3 times
)
print(response.model_dump_json(indent=2))
"""
Output:
{
  "name": "jason",
  "age": 12
}
"""

# *** ADVANCED RETRY LOGIC ***
# Example 2: Retry logic with Tenacity
retries = Retrying(
    stop=stop_after_attempt(2),  # Stop after 2 attempts
    wait=wait_fixed(1),  # Wait 1 second between retries
)


class AdvancedUserDetail(BaseModel):
    name: str
    age: int


response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    response_model=AdvancedUserDetail,
    messages=[{"role": "user", "content": "Extract `Jason is 25 years old`"}],
    max_retries=retries,  # Apply custom retry logic
)

print(response.model_dump_json(indent=2))
"""
Output:
{
  "name": "Jason",
  "age": 25
}
"""


# *** HANDLING RETRY EXCEPTIONS ***
class ValidatedUser(BaseModel):
    name: str
    age: int

    @field_validator("age")
    def validate_age(cls, value: int):
        raise ValueError(f"Invalid age: {value}")


try:
    client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=ValidatedUser,
        messages=[{"role": "user", "content": "Extract `Jason is 25 years old`"}],
        max_retries=retries,
    )
except InstructorRetryException as e:
    print("Validation Error Messages:", e.messages[-1]["content"])  # Last error message
    print("Number of Attempts:", e.n_attempts)  # Total attempts made
    print("Last Completion Object:", e.last_completion)  # Details of the last attempt


# *** ASYNCHRONOUS RETRIES ***
# Asynchronous version of the retry logic
async_client = instructor.from_openai(openai.AsyncOpenAI(), mode=instructor.Mode.TOOLS)


class AsyncUserDetail(BaseModel):
    name: str
    age: int


async_task = async_client.chat.completions.create(
    model="gpt-4-turbo-preview",
    response_model=AsyncUserDetail,
    messages=[{"role": "user", "content": "Extract `Jason is 12`"}],
    max_retries=AsyncRetrying(
        stop=stop_after_attempt(3),  # Stop after 3 attempts
        wait=wait_fixed(1),  # Wait 1 second between attempts
    ),
)

import asyncio

response = asyncio.run(async_task)
print(response.model_dump_json(indent=2))


# *** RETRY CALLBACKS ***
# Logging retries with callbacks
class UserWithLogging(BaseModel):
    name: str
    age: int

    @field_validator("name")
    def name_is_uppercase(cls, value: str):
        assert value.isupper(), "Name must be uppercase"
        return value


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_retries=Retrying(
        stop=stop_after_attempt(3),
        wait=wait_random(0, 1),  # Random wait between 0 and 1 second
        before=lambda retry_state: print("Before:", retry_state),
        after=lambda retry_state: print("After:", retry_state),
    ),
    messages=[{"role": "user", "content": "Extract John is 18 years old"}],
    response_model=UserWithLogging,
)
print(response)


# *** OTHER TENACITY FEATURES ***
# Retry logic with exponential backoff
exponential_retries = Retrying(
    stop=stop_after_attempt(4),  # Stop after 4 attempts
    wait=wait_exponential(
        multiplier=1, min=2, max=10
    ),  # Exponential backoff between 2 and 10 seconds
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=UserResponse,
    messages=[{"role": "user", "content": "Extract Jason is 35"}],
    max_retries=exponential_retries,
)
print(response.model_dump_json(indent=2))
