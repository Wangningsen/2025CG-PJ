import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-1))
w1=cq.Workplane('XY',origin=(0,0,12))
r=w0.sketch().segment((10,56),(64,56)).arc((69,69),(82,74)).segment((82,100)).arc((70,92),(63,78)).segment((10,78)).close().assemble().finalize().extrude(48).union(w1.sketch().push([(-47,-65)]).circle(35).push([(-46,-64)]).rect(66,4,mode='s').finalize().extrude(-59))