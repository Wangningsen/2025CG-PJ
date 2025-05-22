import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
r=w0.sketch().segment((-91,-66),(-9,-100)).segment((7,-68)).segment((29,-80)).segment((64,-30)).segment((46,-16)).segment((63,13)).segment((-17,31)).segment((-24,17)).segment((-26,18)).segment((-38,-2)).segment((-63,1)).close().assemble().finalize().extrude(-37).union(w0.workplane(offset=-11/2).moveTo(53,45).box(76,110,11))