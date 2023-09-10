import typing
import ibis
import ark

@ibis.filters.register("numeric_sort")
def format_float(nodes: typing.Sequence[ark.nodes.Node]):
    return sorted(nodes, key=lambda n: int(n.stem) if n.stem.isnumeric() else -1)
