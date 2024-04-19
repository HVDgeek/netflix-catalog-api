import unittest
from uuid import UUID
import uuid
from category import Category

class TestCategory(unittest.TestCase):
    def setUp(self) -> None:
        self.new_category_id = uuid.uuid4()
        self.new_name = "Filme"
        self.new_description = "Categoria que representa os filmes"

        super().setUp()
    
    def test_name_is_required(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_256_characters(self):
        with self.assertRaisesRegex(ValueError, "name must have less than 256 characters"):
            Category(name="a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name=self.new_name)
        self.assertEqual(type(category.id), UUID)

    def test_category_must_be_created_with_default_values(self):
        category = Category(name=self.new_name)
        self.assertEqual(category.name, self.new_name)
        self.assertEqual(category.description, "")
        self.assertEqual(category.is_active, True)
    
    def test_category_must_be_created_with_is_active_by_default(self):
         category = Category(name=self.new_name)
         self.assertEqual(category.is_active, True)

    def test_category_is_created_with_provided_values(self):
        category = Category(
            id=self.new_category_id,
            name=self.new_name,
            description=self.new_description,
            is_active= False
        )

        self.assertEqual(category.id, self.new_category_id)
        self.assertEqual(category.description, self.new_description)
        self.assertEqual(category.name, self.new_name )
        self.assertEqual(category.is_active, False)

    def test_category_str_method_return_correct_string(self):
        category = Category(
            name=self.new_name,
            description=self.new_description,
        )

        expected_string = f"{self.new_name} - {self.new_description} (True)"
        actual_string = f"{category}" # str(category)

        self.assertEqual(actual_string, expected_string, 
                         f"A representação da categoria está incorreta. "
                         f"Expected: '{expected_string}', "
                         f"Obtained: '{actual_string}'.")


    def test_category_repr_method_return_correct_string(self):
        category = Category(id=self.new_category_id, name=self.new_name)

        expected_repr = f"<Category {self.new_name} {self.new_category_id}>"
        actual_repr = repr(category)

        self.assertEqual(actual_repr, expected_repr, 
                         f"Expected category __repr__ to be '{expected_repr}' but got '{actual_repr}'."
                         )
        

if __name__ == "__main__":
    unittest.main()