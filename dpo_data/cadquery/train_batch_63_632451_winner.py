import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().rect(186,174).push([(-64.5,-51)]).rect(13,34,mode='s').reset().face(w0.sketch().segment((-67,44),(-56,-57)).segment((-25,-55)).arc((10,-60),(42,-46)).segment((67,-44)).segment((56,57)).segment((25,55)).arc((-10,60),(-42,46)).close().assemble(),mode='s').push([(-69,-63.5)]).rect(12,7,mode='s').finalize().extrude(200)