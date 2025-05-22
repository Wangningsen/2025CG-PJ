import cadquery as cq
w0=cq.Workplane('YZ',origin=(12,0,0))
w1=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().segment((-100,-87),(15,-87)).segment((15,-65)).arc((64,-24),(34,34)).arc((21,38),(9,38)).arc((9,37),(8,37)).segment((8,87)).segment((-77,87)).segment((-77,-16)).segment((-39,-16)).arc((-36,-26),(-32,-36)).arc((-28,-45),(-21,-53)).segment((-17,-53)).segment((-17,-56)).segment((-100,-56)).close().assemble().finalize().extrude(-58).union(w0.workplane(offset=34/2).moveTo(76,-16).cylinder(34,8)).union(w1.workplane(offset=68/2).moveTo(8,89).cylinder(68,11))