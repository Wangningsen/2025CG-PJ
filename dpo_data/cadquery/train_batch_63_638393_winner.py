import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.sketch().arc((-92,6),(-58,-88),(32,-41)).segment((33,-41)).segment((33,-14)).segment((100,-14)).segment((100,99)).segment((-92,99)).close().assemble().push([(-89,-92)]).circle(7).push([(-89.5,-92)]).rect(1,6,mode='s').push([(4,42)]).rect(96,80,mode='s').finalize().extrude(76)