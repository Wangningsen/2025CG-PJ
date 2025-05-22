import cadquery as cq
w0=cq.Workplane('YZ',origin=(-45,0,0))
r=w0.sketch().arc((-35,41),(-87,-60),(24,-37)).arc((56,-26),(77,-3)).arc((100,9),(83,27)).arc((31,84),(-35,41)).assemble().reset().face(w0.sketch().arc((72,13),(73,14),(73,16)).arc((71,15),(72,13)).assemble(),mode='s').reset().face(w0.sketch().arc((84,10),(91,7),(85,12)).arc((84,11),(84,10)).assemble(),mode='s').finalize().extrude(90)