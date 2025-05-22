import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
w1=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().push([(-26,48)]).circle(11).rect(2,18,mode='s').finalize().extrude(-34).union(w0.workplane(offset=42/2).moveTo(53.5,-29).box(93,86,42)).union(w1.sketch().segment((35,-16),(61,-16)).segment((61,-7)).arc((72,12),(61,32)).segment((61,41)).segment((35,41)).segment((35,32)).arc((25,12),(35,-7)).close().assemble().finalize().extrude(-75))