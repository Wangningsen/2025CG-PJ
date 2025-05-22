import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
w1=cq.Workplane('XY',origin=(0,0,-23))
r=w0.sketch().push([(-1.5,58.5)]).rect(7,83).push([(-1,58.5)]).rect(6,5,mode='s').finalize().extrude(55).union(w0.sketch().segment((2,2),(6,0)).segment((6,-100)).segment((39,-100)).segment((39,-9)).segment((53,-11)).segment((59,23)).segment((37,23)).segment((37,65)).segment((56,65)).segment((56,26)).segment((71,87)).segment((22,98)).close().assemble().finalize().extrude(55)).union(w1.sketch().push([(-32,14)]).circle(40).circle(36,mode='s').finalize().extrude(-19))