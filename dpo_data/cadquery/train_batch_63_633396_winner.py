import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-44))
w1=cq.Workplane('ZX',origin=(0,20,0))
r=w0.sketch().segment((-23,14),(39,-9)).segment((69,78)).segment((7,100)).close().assemble().finalize().extrude(75).union(w0.workplane(offset=123/2).moveTo(-64.5,-63.5).box(9,73,123)).union(w1.sketch().segment((-79,15),(-74,15)).segment((-74,-23)).segment((-19,-23)).segment((-19,15)).segment((-15,15)).segment((-15,29)).segment((-19,29)).segment((-19,69)).segment((-74,69)).segment((-74,29)).segment((-79,29)).close().assemble().push([(-47,23)]).circle(7,mode='s').finalize().extrude(52))