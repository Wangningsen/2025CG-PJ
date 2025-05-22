import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
r=w0.sketch().segment((-89,-79),(-55,-79)).segment((-55,-100)).segment((16,-100)).segment((16,-79)).segment((49,-79)).segment((49,-33)).segment((89,-33)).segment((89,100)).segment((29,100)).segment((29,36)).segment((16,36)).segment((16,57)).segment((-55,57)).segment((-55,36)).segment((-89,36)).close().assemble().finalize().extrude(10)