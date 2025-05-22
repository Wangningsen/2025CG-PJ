import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-87))
r=w0.sketch().segment((-82,8),(-64,8)).arc((-24,-19),(18,8)).segment((39,8)).segment((39,36)).segment((44,36)).segment((44,-100)).segment((74,-100)).segment((75,31)).segment((82,31)).segment((82,92)).segment((39,92)).segment((39,100)).segment((-82,100)).close().assemble().finalize().extrude(174)