import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-27))
r=w0.sketch().segment((-84,-100),(59,-100)).segment((59,-99)).arc((54,-95),(51,-90)).arc((22,-63),(54,-37)).arc((64,-49),(81,-50)).segment((81,-56)).arc((82,-56),(84,-55)).segment((84,4)).segment((68,4)).segment((68,100)).segment((54,100)).segment((54,4)).segment((-84,4)).close().assemble().finalize().extrude(54)