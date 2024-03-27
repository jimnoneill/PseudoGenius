import unittest
from pseudogenius.genes import Gene, NormalGene, PseudoFrameShift, PseudoIncomplete, PseudoStop, PseudoMulti, Pseudos, process_genes

class TestGeneClasses(unittest.TestCase):

    def setUp(self):
        # Setup mock data for tests
        self.mock_feature = {
            'qualifiers': {
                'locus_tag': ['mock_locus'],
                'translation': ['MRT']
            },
            'location': MockLocation()
        }
        self.mock_parent_sequence = MockSequence('ACTG')

    def test_gene_initialization(self):
        gene = Gene(self.mock_feature, self.mock_parent_sequence)
        self.assertEqual(gene.locus_tag, 'mock_locus')
        self.assertEqual(gene.sequence, 'ACTG')
        self.assertEqual(gene.amino_acids, 'MRT')

    # Add more tests for other classes and functions

# Mock classes to simulate BioPython behavior
class MockLocation:
    def extract(self, parent_sequence):
        return parent_sequence

class MockSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

if __name__ == '__main__':
    unittest.main()
