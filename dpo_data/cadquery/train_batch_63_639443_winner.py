import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
w1=cq.Workplane('XY',origin=(0,0,47))
r=w0.sketch().push([(-47,-65)]).circle(35).push([(-47,-64)]).rect(74,4,mode='s').finalize().extrude(-59).union(w1.sketch().segment((10,56),(64,56)).arc((68,68),(82,74)).segment((82,100)).arc((71,93),(63,78)).segment((10,78)).close().assemble().finalize().extrude(-48))