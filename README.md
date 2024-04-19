# Netflix Catalog API

## Category Entity

This Python module implements a `Category` class representing a category with a name, description, and an activation status.

### Business Rule

- A category must have a name.
- The name of the category must have less than 256 characters.
- When a category is created, it must be assigned a UUID as its identifier.
- A category is created with default values if no additional values are provided.
- The default value for the is_active attribute is True.
- The string representation of a category follows the format: `<name> - <description> (<is_active>)`.
  The representation of a category (`__repr__` method) follows the format: `<Category <name> <id>>`.

### Test Cases

The following test cases are implemented to ensure the correctness of the Category class:

- [x] Test Name is Required

  - Description: Ensure that an error is raised when trying to create a category without providing a name.
  - Expected Result: TypeError with message "missing 1 required positional argument: 'name'".

- [x] Test Name Length Limit

  - Description: Ensure that an error is raised when the name provided for a category exceeds 255 characters.
  - Expected Result: ValueError with message "name must have less than 256 characters".

- [x] Test Category Creation with UUID

  - Description: Ensure that a category is created with a UUID as its identifier.
  - Expected Result: The id attribute of the created category is of type UUID.

- [x] Test Default Category Creation

  - Description: Ensure that a category is created with default values when no additional values are provided.
  - Expected Result: The category has an empty description and is active.

- [x] Test Category Creation with Provided Values

  - Description: Ensure that a category is created with the provided values.
  - Expected Result: The category has the provided attributes.

- [x] Test String Representation

  - Description: Ensure that the string representation of a category is correct.
  - Expected Result: The string representation matches the expected format.

- [x] Test Representation Method (**repr**)
  - Description: Ensure that the representation method returns the correct string.
  - Expected Result: The representation string matches the expected format.
