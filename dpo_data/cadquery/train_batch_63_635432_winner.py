import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
r=w0.sketch().arc((-14,29),(-41,-88),(64,-31)).segment((67,-31)).segment((67,12)).segment((45,12)).arc((39,18),(33,23)).segment((33,40)).segment((67,40)).segment((67,100)).segment((-14,100)).close().assemble().push([(-2,-34)]).circle(14,mode='s').push([(45,70)]).circle(6,mode='s').finalize().extrude(-16)