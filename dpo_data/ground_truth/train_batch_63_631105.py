import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-27))
r=w0.sketch().segment((-84,-100),(59,-100)).segment((15,-73)).segment((41,-30)).segment((54,-38)).segment((54,-50)).segment((68,-50)).segment((68,-47)).segment((84,-56)).segment((84,4)).segment((68,4)).segment((68,100)).segment((54,100)).segment((54,4)).segment((-84,4)).close().assemble().finalize().extrude(54)