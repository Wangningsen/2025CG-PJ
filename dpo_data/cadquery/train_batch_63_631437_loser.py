import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
r=w0.sketch().arc((39,59),(49,60),(58,57)).arc((65,59),(75,59)).arc((58,72),(39,79)).arc((-23,75),(39,74)).close().assemble().finalize().extrude(-32).union(w0.sketch().arc((-33,-7),(-43,-98),(-9,-13)).segment((-9,20)).segment((-33,20)).close().assemble().finalize().extrude(100))