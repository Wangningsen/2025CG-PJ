import cadquery as cq
w0=cq.Workplane('YZ',origin=(-36,0,0))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().push([(-17,34)]).circle(44).push([(-17,34.5)]).rect(28,37,mode='s').push([(-5.5,-48)]).rect(15,70).finalize().extrude(-47).union(w0.workplane(offset=11/2).moveTo(-61,-70).cylinder(11,30)).union(w1.sketch().arc((7,56),(99,45),(20,-4)).segment((66,-4)).segment((66,13)).arc((67,22),(66,30)).segment((66,47)).segment((24,47)).segment((24,56)).close().assemble().finalize().extrude(77))