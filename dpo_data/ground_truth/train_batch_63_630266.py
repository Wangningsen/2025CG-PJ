import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
w1=cq.Workplane('ZX',origin=(0,86,0))
r=w0.sketch().segment((-86,-49),(-54,-79)).segment((-41,-66)).segment((-73,-36)).close().assemble().finalize().extrude(-127).union(w1.workplane(offset=-67/2).moveTo(54,75).cylinder(67,25))