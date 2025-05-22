import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,46))
r=w0.sketch().segment((-49,-15),(8,-15)).segment((44,-47)).arc((48,-31),(44,-15)).segment((73,-15)).segment((73,8)).segment((-49,8)).close().assemble().push([(12,-3)]).circle(7,mode='s').finalize().extrude(-146).union(w0.sketch().push([(-39,13)]).circle(34).push([(-43.5,41)]).rect(5,4,mode='s').finalize().extrude(54))