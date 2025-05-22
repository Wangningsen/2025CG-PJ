import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
w1=cq.Workplane('YZ',origin=(-36,0,0))
r=w0.sketch().push([(-24,0)]).circle(47).push([(-24.5,0)]).rect(65,38,mode='s').finalize().extrude(-121).union(w0.sketch().arc((-85,19),(-53,12),(-23,22)).segment((-46,22)).segment((-46,19)).segment((-48,19)).segment((-48,22)).segment((-85,22)).close().assemble().finalize().extrude(55)).union(w0.sketch().push([(-24,0)]).circle(54).push([(-23.5,13)]).rect(45,16,mode='s').finalize().extrude(79)).union(w1.workplane(offset=121/2).moveTo(32,33).box(36,86,121))