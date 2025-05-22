import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
r=w0.workplane(offset=-106/2).box(58,116,106).union(w0.sketch().segment((-49,-54),(-12,-54)).segment((-12,-61)).segment((12,-61)).segment((12,-54)).segment((49,-54)).segment((49,54)).segment((12,54)).segment((12,61)).segment((-12,61)).segment((-12,54)).segment((-49,54)).close().assemble().rect(82,38,mode='s').finalize().extrude(94))