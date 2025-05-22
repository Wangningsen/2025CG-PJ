import cadquery as cq
w0=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.sketch().segment((-69,-38),(-41,-38)).segment((-41,-100)).segment((41,-100)).segment((41,-38)).segment((69,-38)).segment((69,38)).segment((41,38)).segment((41,100)).segment((-41,100)).segment((-41,38)).segment((-69,38)).close().assemble().finalize().extrude(18)