import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,87))
r=w0.sketch().segment((-82,8),(-63,8)).arc((-20,-19),(24,8)).segment((44,8)).segment((44,-100)).segment((74,-100)).segment((75,36)).segment((39,36)).segment((39,100)).segment((-82,100)).close().assemble().finalize().extrude(-174).union(w0.workplane(offset=-162/2).moveTo(20,63).box(124,58,162))