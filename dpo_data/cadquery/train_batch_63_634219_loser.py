import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,35))
w1=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().push([(-25,49)]).circle(11).push([(-24.5,48.5)]).rect(3,13,mode='s').finalize().extrude(-76).union(w0.workplane(offset=-42/2).moveTo(53.5,-29).box(93,86,42)).union(w1.sketch().segment((35,-16),(61,-16)).segment((61,-7)).arc((72,12),(61,32)).segment((61,41)).segment((35,41)).segment((35,32)).arc((25,12),(35,-7)).close().assemble().finalize().extrude(-75))