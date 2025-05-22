import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-72,-22),(-21,-35)).arc((-8,-40),(6,-41)).segment((55,-53)).segment((72,19)).segment((46,26)).arc((15,52),(-26,43)).segment((-55,51)).close().assemble().finalize().extrude(200)