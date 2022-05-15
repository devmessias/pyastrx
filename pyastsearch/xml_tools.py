import re
from lxml import etree


regex_ns = etree.FunctionNamespace("https://github.com/hchasestevens/astpath")
regex_ns.prefix = "re"


@regex_ns
def match(ctx, pattern, strings):
    return any(re.match(pattern, s) is not None for s in strings)


@regex_ns
def search(ctx, pattern, strings):
    return any(re.search(pattern, s) is not None for s in strings)


def linenos_from_xml(elements, node_mappings=None):
    """Given a list of elements, return a list of line numbers."""
    lines = []
    for element in elements:
        try:
            linenos = element.xpath("./ancestor-or-self::*[@lineno][1]/@lineno")
            col_offset = element.xpath("./ancestor-or-self::*[@col_offset][1]/@col_offset")
        except AttributeError:
            raise AttributeError("Element has no ancestor with line number.")
        except SyntaxError:
            # we're not using lxml backend
            if node_mappings is None:
                raise ValueError(
                    "Lines cannot be returned when using native "
                    "backend without `node_mappings` supplied."
                )
            linenos = (getattr(node_mappings[element], "lineno", 0),)

        if linenos:
            col = col_offset[0] if col_offset else 0
            lines.append((int(linenos[0]), int(col)))

    return lines
