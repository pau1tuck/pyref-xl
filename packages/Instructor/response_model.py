# Complete Instructor response model with prompting, optional values, dynamic creating, and behaviors.

from pydantic import BaseModel, Field, create_model
from typing import Optional, Literal, List
from openai import OpenAI
import instructor

# Initialize the Instructor client
client = instructor.from_openai(OpenAI())


# *** Prompting ***
class User(BaseModel):
    """
    Represents a user for generating responses.
    This docstring will be included in the prompt for the language model.
    """

    name: str = Field(description="The full name of the user.")
    age: int = Field(description="The user's age in years.")
    email: Optional[str] = Field(
        default=None, description="The user's email address, if available."
    )
    active: bool = Field(description="Whether the user is currently active.")

    def deactivate(self):
        """
        Custom behavior to deactivate the user.
        """
        print(f"Deactivating user: {self.name}")
        self.active = False
        return self.active


# *** Dynamic Model Creation ***
DynamicUserModel = create_model(
    "DynamicUserModel",
    address=(str, None),  # Optional address field
    phone=(Optional[str], None),  # Optional phone field
    is_admin=(bool, False),  # Default value for admin status
    __base__=User,  # Inherit fields and behavior from `User`
)


# Add a method dynamically to the new model
def promote_to_admin(self):
    """
    Promote a user to admin.
    """
    print(f"Promoting user: {self.name} to admin.")
    self.is_admin = True
    return self.is_admin


DynamicUserModel.promote_to_admin = promote_to_admin


# *** Combined Example with Prompting, Optional Values, and Behavior ***
class SearchQuery(BaseModel):
    """
    Represents a search query to the language model.
    """

    query: str = Field(description="The search query string.")
    query_type: Literal["web", "image", "video"] = Field(
        description="The type of search (web, image, or video)."
    )
    results: Optional[List[str]] = Field(
        default=None, description="The list of search results."
    )

    def execute(self):
        """
        Execute the search query and return mock results.
        """
        print(f"Executing search for '{self.query}' with type '{self.query_type}'.")
        # For demonstration purposes, returning mock results
        return [f"{self.query} result {i}" for i in range(1, 4)]


# *** Use Case: Creating a Response Model ***
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Search for pictures of cute puppies"}],
    response_model=SearchQuery,
)

# Execute the search query
search_results = response.execute()
print(
    search_results
)  # Output: ['cute puppies result 1', 'cute puppies result 2', 'cute puppies result 3']

# Example usage of dynamic user model
dynamic_user = DynamicUserModel(
    name="John Doe", age=30, email="john.doe@example.com", active=True
)
dynamic_user.promote_to_admin()  # Promotes the user to admin
print(dynamic_user.is_admin)  # Output: True

dynamic_user.deactivate()  # Deactivates the user
print(dynamic_user.active)  # Output: False
