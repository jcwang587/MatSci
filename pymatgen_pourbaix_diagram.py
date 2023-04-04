from mp_api.client import MPRester
from pymatgen.analysis.pourbaix_diagram import PourbaixDiagram, ELEMENTS_HO, PourbaixPlotter

mpr = MPRester("zUkBM3Sid3ny0pDHwf1uFVlPLloCW5Df")

entry = mpr.get_entries("mp-2647047")[0]
composition = entry.composition
comp_dict = {str(key): value for key, value in composition.items() if key not in ELEMENTS_HO}

data = mpr.get_pourbaix_entries(list(comp_dict.keys()))

pbx = PourbaixDiagram(data, comp_dict=comp_dict, filter_solids=True)
plt = PourbaixPlotter(pbx).get_pourbaix_plot()
