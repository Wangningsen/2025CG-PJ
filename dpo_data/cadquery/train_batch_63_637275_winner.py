import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-75,47),(-28,-40),(76,-6)).arc((58,-10),(43,5)).segment((18,-27)).close().assemble().finalize().extrude(-200)