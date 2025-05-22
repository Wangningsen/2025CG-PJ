import cadquery as cq
w0=cq.Workplane('YZ',origin=(-65,0,0))
r=w0.sketch().push([(-35.5,0)]).rect(129,122).push([(-78,41)]).circle(3,mode='s').finalize().extrude(110).union(w0.sketch().segment((15,18),(58,-25)).segment((82,-8)).segment((100,-8)).segment((100,19)).segment((81,19)).segment((43,55)).close().assemble().push([(29,-3)]).circle(3,mode='s').finalize().extrude(130))