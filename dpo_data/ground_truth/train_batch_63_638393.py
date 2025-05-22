import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.sketch().arc((-92,6),(-44,-92),(32,-14)).segment((100,-14)).segment((100,99)).segment((-92,99)).close().assemble().push([(4,42)]).rect(96,80,mode='s').push([(-92,-92)]).circle(7).finalize().extrude(76)