#!/usr/bin/env python3

import os
import unittest
from collections import deque

import pdfplumber
from pdfplumber.structure import PDFStructTree

HERE = os.path.abspath(os.path.dirname(__file__))
TREE = [
    {
        "type": "Document",
        "children": [
            {
                "type": "P",
                "attributes": {
                    "O": "Layout",
                    "Placement": "Block",
                    "SpaceBefore": 0.24,
                    "TextAlign": "Center",
                },
                "mcids": [0],
            },
            {
                "type": "H1",
                "attributes": {
                    "O": "Layout",
                    "Placement": "Block",
                    "SpaceBefore": 0.36,
                },
                "mcids": [1],
            },
            {
                "type": "P",
                "attributes": {
                    "O": "Layout",
                    "Placement": "Block",
                    "SpaceBefore": 0.12,
                },
                "mcids": [2],
            },
            {
                "type": "P",
                "attributes": {
                    "O": "Layout",
                    "Placement": "Block",
                    "SpaceBefore": 0.181,
                },
                "mcids": [3, 4, 5, 6, 7],
            },
            {
                "type": "H2",
                "attributes": {
                    "O": "Layout",
                    "Placement": "Block",
                    "SpaceBefore": 0.381,
                },
                "mcids": [8],
            },
            {
                "type": "P",
                "attributes": {
                    "O": "Layout",
                    "Placement": "Block",
                    "SpaceBefore": 0.12,
                },
                "mcids": [9],
            },
            {
                "type": "L",
                "children": [
                    {
                        "type": "LI",
                        "children": [
                            {
                                "type": "LBody",
                                "children": [
                                    {
                                        "type": "P",
                                        "attributes": {
                                            "O": "Layout",
                                            "Placement": "Block",
                                            "SpaceBefore": 0.181,
                                            "StartIndent": 0.36,
                                        },
                                        "mcids": [10, 11],
                                    }
                                ],
                            }
                        ],
                    },
                    {
                        "type": "LI",
                        "children": [
                            {
                                "type": "LBody",
                                "children": [
                                    {
                                        "type": "P",
                                        "attributes": {
                                            "O": "Layout",
                                            "Placement": "Block",
                                            "SpaceBefore": 0.181,
                                            "StartIndent": 0.36,
                                        },
                                        "mcids": [12, 13],
                                    },
                                    {
                                        "type": "L",
                                        "children": [
                                            {
                                                "type": "LI",
                                                "children": [
                                                    {
                                                        "type": "LBody",
                                                        "children": [
                                                            {
                                                                "type": "P",
                                                                "attributes": {
                                                                    "O": "Layout",
                                                                    "Placement": "Block",  # noqa: E501
                                                                    "SpaceBefore": 0.181,  # noqa: E501
                                                                    "StartIndent": 0.72,  # noqa: E501
                                                                },
                                                                "mcids": [14, 15],
                                                            }
                                                        ],
                                                    }
                                                ],
                                            }
                                        ],
                                    },
                                ],
                            }
                        ],
                    },
                    {
                        "type": "LI",
                        "children": [
                            {
                                "type": "LBody",
                                "children": [
                                    {
                                        "type": "P",
                                        "attributes": {
                                            "O": "Layout",
                                            "Placement": "Block",
                                            "SpaceBefore": 0.181,
                                            "StartIndent": 0.36,
                                        },
                                        "mcids": [16, 17, 18, 19, 20, 21, 22, 23],
                                    }
                                ],
                            }
                        ],
                    },
                ],
            },
            {
                "type": "H3",
                "attributes": {
                    "O": "Layout",
                    "Placement": "Block",
                    "SpaceBefore": 0.321,
                },
                "mcids": [24],
            },
            {
                "type": "Table",
                "attributes": {
                    "O": "Layout",
                    "Placement": "Block",
                    "SpaceBefore": 0.12,
                    "SpaceAfter": 0.015,
                    "Width": 9.972,
                    "Height": 1.047,
                    "BBox": [56.7, 249.75, 555.3, 302.1],
                },
                "children": [
                    {
                        "type": "TR",
                        "attributes": {"O": "Layout", "Placement": "Block"},
                        "children": [
                            {
                                "type": "TH",
                                "attributes": {
                                    "O": "Layout",
                                    "Placement": "Inline",
                                    "Width": 4.985,
                                    "Height": 0.291,
                                },
                                "children": [
                                    {
                                        "type": "P",
                                        "attributes": {
                                            "O": "Layout",
                                            "Placement": "Block",
                                        },
                                        "mcids": [25],
                                    }
                                ],
                            },
                            {
                                "type": "TH",
                                "attributes": {
                                    "O": "Layout",
                                    "Placement": "Inline",
                                    "Width": 4.987,
                                    "Height": 0.291,
                                },
                                "children": [
                                    {
                                        "type": "P",
                                        "attributes": {
                                            "O": "Layout",
                                            "Placement": "Block",
                                        },
                                        "mcids": [26],
                                    }
                                ],
                            },
                        ],
                    },
                    {
                        "type": "TR",
                        "attributes": {"O": "Layout", "Placement": "Block"},
                        "children": [
                            {
                                "type": "TD",
                                "attributes": {
                                    "O": "Layout",
                                    "Placement": "Inline",
                                    "Width": 4.985,
                                    "Height": 0.291,
                                },
                                "children": [
                                    {
                                        "type": "P",
                                        "attributes": {
                                            "O": "Layout",
                                            "Placement": "Block",
                                        },
                                        "mcids": [27],
                                    }
                                ],
                            },
                            {
                                "type": "TD",
                                "attributes": {
                                    "O": "Layout",
                                    "Placement": "Inline",
                                    "Width": 4.987,
                                    "Height": 0.291,
                                },
                                "children": [
                                    {
                                        "type": "P",
                                        "attributes": {
                                            "O": "Layout",
                                            "Placement": "Block",
                                        },
                                        "mcids": [28],
                                    }
                                ],
                            },
                        ],
                    },
                    {
                        "type": "TR",
                        "attributes": {"O": "Layout", "Placement": "Block"},
                        "children": [
                            {
                                "type": "TD",
                                "attributes": {
                                    "O": "Layout",
                                    "Placement": "Inline",
                                    "Width": 4.985,
                                    "Height": 0.33,
                                },
                                "children": [
                                    {
                                        "type": "P",
                                        "attributes": {
                                            "O": "Layout",
                                            "Placement": "Block",
                                        },
                                        "mcids": [29],
                                    }
                                ],
                            },
                            {
                                "type": "TD",
                                "attributes": {
                                    "O": "Layout",
                                    "Placement": "Inline",
                                    "Width": 4.987,
                                    "Height": 0.33,
                                },
                                "children": [
                                    {
                                        "type": "P",
                                        "attributes": {
                                            "O": "Layout",
                                            "Placement": "Block",
                                        },
                                        "mcids": [30],
                                    }
                                ],
                            },
                        ],
                    },
                ],
            },
        ],
    }
]


class Test(unittest.TestCase):
    """Test a PDF specifically created to show structure."""

    @classmethod
    def setup_class(self):
        path = os.path.join(HERE, "pdfs/pdf_structure.pdf")
        self.pdf = pdfplumber.open(path)

    @classmethod
    def teardown_class(self):
        self.pdf.close()

    def test_structure_tree(self):
        assert self.pdf.pages[0].structure_tree == TREE
        # Add page numbers
        d = deque(TREE)
        while d:
            el = d.popleft()
            el["page_number"] = 1
            if "children" in el:
                d.extend(el["children"])
        assert self.pdf.structure_tree == TREE


PVSTRUCT = [
    {
        "type": "Sect",
        "children": [
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [0]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [1]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [2]},
            {"type": "P", "lang": "FR-FR", "page_number": 1, "mcids": [3]},
            {"type": "P", "lang": "FR-FR", "page_number": 1, "mcids": [4]},
            {"type": "P", "lang": "FR-FR", "page_number": 1, "mcids": [5]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [6]},
            {"type": "P", "lang": "FR-FR", "page_number": 1, "mcids": [7]},
            {
                "type": "P",
                "lang": "FR-FR",
                "page_number": 1,
                "mcids": [8],
                "children": [
                    {"type": "Span", "lang": "FR-CA", "page_number": 1, "mcids": [9]}
                ],
            },
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [11]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [12]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [13]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [14]},
            {"type": "P", "lang": "FR-FR", "page_number": 1, "mcids": [15]},
            {"type": "P", "lang": "FR-FR", "page_number": 1, "mcids": [16]},
            {
                "type": "L",
                "children": [
                    {
                        "type": "LI",
                        "children": [
                            {
                                "type": "LBody",
                                "lang": "FR-CA",
                                "page_number": 1,
                                "mcids": [19],
                            }
                        ],
                    }
                ],
            },
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [22]},
            {"type": "P", "lang": "FR-FR", "page_number": 1, "mcids": [23]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [24]},
            {
                "type": "L",
                "children": [
                    {
                        "type": "LI",
                        "children": [
                            {
                                "type": "LBody",
                                "lang": "FR-CA",
                                "page_number": 1,
                                "mcids": [27],
                            }
                        ],
                    }
                ],
            },
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [30]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [31]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [32]},
            {
                "type": "L",
                "children": [
                    {
                        "type": "LI",
                        "children": [
                            {
                                "type": "LBody",
                                "lang": "FR-CA",
                                "page_number": 1,
                                "mcids": [35],
                            }
                        ],
                    }
                ],
            },
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [38]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [39]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [40]},
            {
                "type": "L",
                "children": [
                    {
                        "type": "LI",
                        "children": [
                            {
                                "type": "LBody",
                                "lang": "FR-CA",
                                "page_number": 1,
                                "mcids": [43, 45],
                                "children": [
                                    {
                                        "type": "Span",
                                        "lang": "FR-FR",
                                        "page_number": 1,
                                        "mcids": [44],
                                    }
                                ],
                            }
                        ],
                    }
                ],
            },
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [48]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [49]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [50]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [51]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [52]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [53]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [54]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [55]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [56]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [57]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [58]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [59]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [60]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [61]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [62]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [63]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [64]},
            {"type": "P", "lang": "FR-CA", "page_number": 1, "mcids": [65]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [0]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [1]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [2]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [3]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [4]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [5]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [6]},
            {
                "type": "L",
                "children": [
                    {
                        "type": "LI",
                        "children": [
                            {
                                "type": "LBody",
                                "lang": "FR-CA",
                                "page_number": 2,
                                "mcids": [9, 11],
                                "children": [
                                    {
                                        "type": "Span",
                                        "lang": "FR-FR",
                                        "page_number": 2,
                                        "mcids": [10],
                                    }
                                ],
                            }
                        ],
                    }
                ],
            },
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [14]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [15]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [16]},
            {"type": "P", "lang": "FR-FR", "page_number": 2, "mcids": [17]},
            {"type": "P", "lang": "FR-FR", "page_number": 2, "mcids": [18]},
            {"type": "P", "lang": "FR-FR", "page_number": 2, "mcids": [19]},
        ],
    }
]


PVSTRUCT1 = [
    {
        "type": "Sect",
        "children": [
            {"lang": "FR-CA", "type": "P", "mcids": [0]},
            {"lang": "FR-CA", "type": "P", "mcids": [1]},
            {"lang": "FR-CA", "type": "P", "mcids": [2]},
            {"lang": "FR-CA", "type": "P", "mcids": [3]},
            {"lang": "FR-CA", "type": "P", "mcids": [4]},
            {"lang": "FR-CA", "type": "P", "mcids": [5]},
            {"lang": "FR-CA", "type": "P", "mcids": [6]},
            {
                "type": "L",
                "children": [
                    {
                        "type": "LI",
                        "children": [
                            {
                                "lang": "FR-CA",
                                "type": "LBody",
                                "mcids": [9, 11],
                                "children": [
                                    {"lang": "FR-FR", "type": "Span", "mcids": [10]}
                                ],
                            }
                        ],
                    }
                ],
            },
            {"lang": "FR-CA", "type": "P", "mcids": [14]},
            {"lang": "FR-CA", "type": "P", "mcids": [15]},
            {"lang": "FR-CA", "type": "P", "mcids": [16]},
            {"lang": "FR-FR", "type": "P", "mcids": [17]},
            {"lang": "FR-FR", "type": "P", "mcids": [18]},
            {"lang": "FR-FR", "type": "P", "mcids": [19]},
        ],
    }
]

PVSTRUCT2 = [
    {
        "type": "Sect",
        "children": [
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [0]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [1]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [2]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [3]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [4]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [5]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [6]},
            {
                "type": "L",
                "children": [
                    {
                        "type": "LI",
                        "children": [
                            {
                                "type": "LBody",
                                "lang": "FR-CA",
                                "page_number": 2,
                                "mcids": [9, 11],
                                "children": [
                                    {
                                        "type": "Span",
                                        "lang": "FR-FR",
                                        "page_number": 2,
                                        "mcids": [10],
                                    }
                                ],
                            }
                        ],
                    }
                ],
            },
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [14]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [15]},
            {"type": "P", "lang": "FR-CA", "page_number": 2, "mcids": [16]},
            {"type": "P", "lang": "FR-FR", "page_number": 2, "mcids": [17]},
            {"type": "P", "lang": "FR-FR", "page_number": 2, "mcids": [18]},
            {"type": "P", "lang": "FR-FR", "page_number": 2, "mcids": [19]},
        ],
    }
]

IMAGESTRUCT = [
    {
        "type": "Document",
        "children": [
            {"type": "P", "mcids": [0]},
            {"type": "P", "mcids": [1]},
            {
                "type": "Figure",
                "alt_text": "pdfplumber on github\n\n"
                "a screen capture of the github page for pdfplumber",
                "mcids": [2],
            },
        ],
    }
]


WORD365 = [
    {
        "type": "Document",
        "children": [
            {
                "type": "H1",
                "children": [
                    {"type": "Span", "mcids": [0]},
                    {"type": "Span", "actual_text": " ", "mcids": [1]},
                ],
            },
            {"type": "P", "mcids": [2]},
            {
                "type": "L",
                "attributes": {"O": "List", "ListNumbering": "Disc"},
                "children": [
                    {"type": "LI", "children": [{"type": "LBody", "mcids": [3]}]},
                    {"type": "LI", "children": [{"type": "LBody", "mcids": [4]}]},
                    {"type": "LI", "children": [{"type": "LBody", "mcids": [5]}]},
                ],
            },
            {"type": "P", "mcids": [6]},
            {
                "type": "L",
                "attributes": {"O": "List", "ListNumbering": "Decimal"},
                "children": [
                    {"type": "LI", "children": [{"type": "LBody", "mcids": [7]}]},
                    {"type": "LI", "children": [{"type": "LBody", "mcids": [8]}]},
                ],
            },
            {
                "type": "Table",
                "children": [
                    {
                        "type": "THead",
                        "children": [
                            {
                                "type": "TR",
                                "children": [
                                    {
                                        "type": "TH",
                                        "children": [{"type": "P", "mcids": [9, 10]}],
                                    },
                                    {
                                        "type": "TH",
                                        "children": [{"type": "P", "mcids": [11, 12]}],
                                    },
                                    {
                                        "type": "TH",
                                        "children": [{"type": "P", "mcids": [13, 14]}],
                                    },
                                ],
                            }
                        ],
                    },
                    {
                        "type": "TBody",
                        "children": [
                            {
                                "type": "TR",
                                "children": [
                                    {
                                        "type": "TD",
                                        "children": [{"type": "P", "mcids": [15, 16]}],
                                    },
                                    {
                                        "type": "TD",
                                        "children": [{"type": "P", "mcids": [17, 18]}],
                                    },
                                    {
                                        "type": "TD",
                                        "children": [{"type": "P", "mcids": [19, 20]}],
                                    },
                                ],
                            },
                            {
                                "type": "TR",
                                "children": [
                                    {
                                        "type": "TD",
                                        "children": [{"type": "P", "mcids": [21, 22]}],
                                    },
                                    {
                                        "type": "TD",
                                        "children": [{"type": "P", "mcids": [23, 24]}],
                                    },
                                    {
                                        "type": "TD",
                                        "children": [{"type": "P", "mcids": [25, 26]}],
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
            {"type": "P", "mcids": [27]},
        ],
    }
]


SCOTUS = [
    {
        "type": "Div",
        "children": [
            {
                "type": "P",
                "page_number": 1,
                "attributes": {
                    "LineHeight": 25.75,
                    "TextIndent": 21.625,
                    "O": "Layout",
                },
                "mcids": [1],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {
                    "LineHeight": 25.75,
                    "StartIndent": 86.375,
                    "O": "Layout",
                },
                "mcids": [2],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {
                    "LineHeight": 25.75,
                    "TextIndent": 50.375,
                    "O": "Layout",
                },
                "mcids": [3, 4],
            },
            {
                "type": "P",
                "page_number": 1,
                # This is important, it has attributes and a class
                "attributes": {
                    "LineHeight": 25.75,
                    "StartIndent": 165.625,
                    "EndIndent": 57.625,
                    "SpaceAfter": 24.5,
                    "O": "Layout",
                },
                "mcids": [5],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {
                    "LineHeight": 25.75,
                    "TextIndent": 100.75,
                    "O": "Layout",
                },
                "mcids": [6],
            },
            {
                "type": "P",
                "page_number": 1,
                # This is important, it has attributes and a class
                "attributes": {
                    "LineHeight": 25.75,
                    "TextIndent": 21.625,
                    "EndIndent": 50.375,
                    "O": "Layout",
                    "TextAlign": "None",
                    "SpaceAfter": 179.125,
                },
                "mcids": [7],
            },
            {
                "type": "P",
                "page_number": 1,
                # This is important, it has two attribute classes
                "attributes": {"O": "Layout", "TextAlign": "Center", "SpaceAfter": 8.5},
                "mcids": [8],
            },
            {
                "type": "P",
                "page_number": 1,
                "attributes": {"O": "Layout", "TextAlign": "Center"},
                "mcids": [9],
            },
        ],
    }
]


HELLO = [
    {
        "type": "Section",
        "page_number": 1,
        "children": [
            {
                "type": "P",
                "page_number": 1,
                "attributes": {"O": "Foo", "A1": 1},
                "mcids": [1],
            },
            {
                "type": "P",
                "page_number": 2,
                "attributes": {"O": "Foo", "A1": 2, "A2": 2},
                "mcids": [1],
            },
        ],
    },
    {
        "type": "P",
        "revision": 1,
        "page_number": 2,
        "attributes": {"O": "Foo", "A1": 3, "A2": 3},
        "mcids": [2],
    },
]
HELLO1 = [
    {
        "type": "Section",
        "page_number": 1,
        "children": [
            {
                "type": "P",
                "page_number": 1,
                "attributes": {"O": "Foo", "A1": 1},
                "mcids": [1],
            },
        ],
    }
]
HELLO1P = [
    {
        "type": "Section",
        "children": [{"type": "P", "attributes": {"O": "Foo", "A1": 1}, "mcids": [1]}],
    }
]


class TestClass(unittest.TestCase):
    """Test the underlying Structure tree class"""

    def test_structure_tree_class(self):
        path = os.path.join(HERE, "pdfs/image_structure.pdf")
        pdf = pdfplumber.open(path)
        stree = PDFStructTree(pdf, pdf.pages[0])
        doc_elem = next(iter(stree))
        assert [k.type for k in doc_elem] == ["P", "P", "Figure"]


class TestUnparsed(unittest.TestCase):
    """Test handling of PDFs with unparsed pages."""

    def test_unparsed_pages(self):
        path = os.path.join(HERE, "pdfs/2023-06-20-PV.pdf")

        pdf = pdfplumber.open(path, pages=[2])
        assert pdf.structure_tree == PVSTRUCT2


class TestMany(unittest.TestCase):
    """Test various PDFs."""

    def test_no_stucture(self):
        path = os.path.join(HERE, "pdfs/pdffill-demo.pdf")
        pdf = pdfplumber.open(path)
        assert pdf.structure_tree == []
        assert pdf.pages[0].structure_tree == []

    def test_word365(self):
        path = os.path.join(HERE, "pdfs/word365_structure.pdf")
        pdf = pdfplumber.open(path)
        page = pdf.pages[0]
        assert page.structure_tree == WORD365

    def test_proces_verbal(self):
        path = os.path.join(HERE, "pdfs/2023-06-20-PV.pdf")

        pdf = pdfplumber.open(path)
        assert pdf.structure_tree == PVSTRUCT
        page = pdf.pages[1]
        assert page.structure_tree == PVSTRUCT1

    def test_image_structure(self):
        path = os.path.join(HERE, "pdfs/image_structure.pdf")

        pdf = pdfplumber.open(path)
        page = pdf.pages[0]
        assert page.structure_tree == IMAGESTRUCT

    def test_figure_mcids(self):
        path = os.path.join(HERE, "pdfs/figure_structure.pdf")

        pdf = pdfplumber.open(path)
        page = pdf.pages[0]
        d = deque(page.structure_tree)
        while d:
            el = d.popleft()
            if el["type"] == "Figure":
                break
            if "children" in el:
                d.extend(el["children"])
        # We found a Figure
        assert el["type"] == "Figure"
        # It has these MCIDS
        assert el["mcids"] == [1, 14]

    def test_scotus(self):
        # This one actually has attribute classes!
        path = os.path.join(HERE, "pdfs/scotus-transcript-p1.pdf")
        pdf = pdfplumber.open(path)
        assert pdf.structure_tree == SCOTUS

    def test_chelsea_pdta(self):
        # This one has structure elements for marked content sections
        path = os.path.join(HERE, "pdfs/chelsea_pdta.pdf")
        pdf = pdfplumber.open(path)
        # This page has no structure tree (really!)
        tree8 = pdf.pages[7].structure_tree
        assert tree8 == []
        # We should also have no structure tree here
        with pdfplumber.open(path, pages=[8]) as pdf8:
            assert pdf8.structure_tree == []
        # This page is empty
        tree3 = pdf.pages[3].structure_tree
        assert tree3 == []
        # This page in particular has OBJR and MCR elements
        tree1 = pdf.pages[2].structure_tree
        assert tree1  # Should contain a tree!
        pdf = pdfplumber.open(path, pages=[3])
        tree2 = pdf.structure_tree
        assert tree2
        # Compare modulo page_number
        d = deque(zip(tree1, tree2))
        while d:
            el1, el2 = d.popleft()
            if "page_number" in el1:
                assert el1["page_number"] == 3
                assert el1 == el2
            if "children" in el1:
                assert len(el1["children"]) == len(el2["children"])
                d.extend(zip(el1["children"], el2["children"]))

    def test_hello_structure(self):
        # Synthetic PDF to test some corner cases
        path = os.path.join(HERE, "pdfs/hello_structure.pdf")
        with pdfplumber.open(path) as pdf:
            assert pdf.structure_tree == HELLO
            assert pdf.pages[0].structure_tree == HELLO1P
        with pdfplumber.open(path, pages=[1]) as pdf:
            assert pdf.structure_tree == HELLO1
