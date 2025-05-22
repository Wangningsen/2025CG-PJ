import cadquery as cq
w0=cq.Workplane('YZ',origin=(14,0,0))
w1=cq.Workplane('XY',origin=(0,0,-18))
r=w0.sketch().segment((-100,29),(-86,13)).segment((-86,-53)).segment((-26,-53)).segment((-24,-56)).segment((-22,-53)).segment((25,-53)).segment((25,-39)).segment((100,-39)).segment((100,56)).segment((25,56)).segment((25,83)).segment((-35,83)).segment((-37,85)).segment((-39,83)).segment((-86,83)).segment((-86,41)).close().assemble().finalize().extrude(-28).union(w1.sketch().arc((3,53),(-5,41),(8,48)).arc((0,46),(3,53)).assemble().finalize().extrude(-67))