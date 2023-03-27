from django.test import TestCase
from .models import Processor
class ProcessorTestCase(TestCase):

    # Testing the CRUD function
    def setUp(self):
        Processor.objects.create(name="Intel Core i9-11900K")
        Processor.objects.create(name="AMD Ryzen 9 5950X")

    def test_create_processor(self):
        """Test creating a new processor"""
        name = "Intel Core i7-11700K"
        processor = Processor.objects.create(name=name)
        self.assertEqual(processor.name, name)

    def test_read_processors(self):
        """Test reading all processors"""
        processors = Processor.objects.all()
        self.assertEqual(processors.count(), 2)

    def test_update_processor(self):
        """Test updating an existing processor"""
        processor = Processor.objects.get(name="Intel Core i9-11900K")
        processor.name = "Intel Core i9-12900K"
        processor.save()
        updated_processor = Processor.objects.get(pk=processor.pk)
        self.assertEqual(updated_processor.name, "Intel Core i9-12900K")

    def test_delete_processor(self):
        """Test deleting an existing processor"""
        processor = Processor.objects.get(name="AMD Ryzen 9 5950X")
        processor.delete()
        processors = Processor.objects.all()
        self.assertEqual(processors.count(), 1)
        self.assertFalse(Processor.objects.filter(name="AMD Ryzen 9 5950X").exists())


