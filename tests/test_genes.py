import unittest
from pseudogenius.genes import process_genes
from pseudogenius.utils import create_dataset

class TestGeneProcessing(unittest.TestCase):
    def test_process_genes(self):
        # This will test the process_genes function by processing a sample GenBank file.
        genes = process_genes('data/sequence.gb')
        # Basic checks to ensure genes dictionary is populated correctly
        self.assertIn('normal_genes', genes)
        self.assertIn('pseudos', genes)
        self.assertTrue(isinstance(genes['normal_genes'], list))
        self.assertTrue(isinstance(genes['pseudos'], list))

    def test_create_dataset(self):
        # This will test the create_dataset function from utils.py.
        # First, process the genes to use as input for create_dataset.
        genes = process_genes('data/sequence.gb')
        dataset = create_dataset(genes)
        # Check if the dataset created is not empty and is a DataFrame.
        self.assertFalse(dataset.empty)

# The following section is a safeguard for running the tests.
if __name__ == '__main__':
    unittest.main()
