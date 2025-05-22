import cadquery as cq
w0=cq.Workplane('YZ',origin=(-36,0,0))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().segment((-13,-83),(2,-83)).segment((2,-13)).arc((-23,77),(-13,-14)).close().assemble().push([(-17,34.5)]).rect(28,37,mode='s').finalize().extrude(-47).union(w0.workplane(offset=11/2).moveTo(-61,-70).cylinder(11,30)).union(w1.sketch().arc((7,56),(14,55),(20,53)).segment((20,47)).segment((66,47)).segment((66,28)).arc((67,21),(66,14)).segment((66,-4)).segment((20,-4)).segment((20,-5)).arc((99,45),(7,56)).assemble().finalize().extrude(77))