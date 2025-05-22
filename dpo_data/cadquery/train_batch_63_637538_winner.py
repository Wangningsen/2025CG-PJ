import cadquery as cq
w0=cq.Workplane('YZ',origin=(4,0,0))
w1=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().push([(-28.5,70)]).rect(65,42).reset().face(w0.sketch().segment((-44,-91),(43,-91)).segment((43,-83)).arc((61,-64),(43,-45)).segment((43,-11)).segment((-44,-11)).close().assemble()).finalize().extrude(-104).union(w1.sketch().segment((-13,0),(-12,0)).segment((-12,-9)).segment((85,-9)).segment((85,0)).segment((100,0)).segment((100,18)).segment((85,18)).segment((85,41)).segment((-12,41)).segment((-12,18)).segment((-13,18)).close().assemble().finalize().extrude(71))