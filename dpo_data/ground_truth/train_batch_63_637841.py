import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-65,58),(-47,42)).arc((-5,32),(28,5)).segment((-6,5)).segment((36,-34)).segment((36,-7)).arc((43,-25),(47,-43)).segment((65,-60)).arc((29,31),(-65,58)).assemble().finalize().extrude(-200)