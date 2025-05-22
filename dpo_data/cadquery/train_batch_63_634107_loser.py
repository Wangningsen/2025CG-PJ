import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
w1=cq.Workplane('YZ',origin=(8,0,0))
r=w0.sketch().segment((19,-19),(21,-19)).arc((45,-45),(72,-19)).segment((74,-19)).segment((74,-17)).segment((72,-17)).arc((45,9),(21,-17)).segment((19,-17)).close().assemble().finalize().extrude(-10).union(w0.sketch().segment((8,-47),(100,-47)).segment((100,-31)).arc((85,-30),(72,-23)).segment((82,-23)).segment((82,9)).segment((8,9)).close().assemble().finalize().extrude(6)).union(w1.workplane(offset=-40/2).moveTo(-55,2).cylinder(40,45))