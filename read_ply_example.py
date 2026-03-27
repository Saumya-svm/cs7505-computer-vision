import os
import sys

def read_with_open3d(file_path):
    try:
        import open3d as o3d
        print("\n--- Reading with Open3D ---")
        pcd = o3d.io.read_point_cloud(file_path)
        print(f"Points: {len(pcd.points)}")
        # If it's a mesh:
        # mesh = o3d.io.read_triangle_mesh(file_path)
        # print(f"Vertices: {len(mesh.vertices)}, Faces: {len(mesh.triangles)}")
        return True
    except ImportError:
        print("Open3D not installed.")
        return False
    except Exception as e:
        print(f"Error reading with Open3D: {e}")
        return False

def read_with_plyfile(file_path):
    try:
        from plyfile import PlyData
        print("\n--- Reading with plyfile ---")
        plydata = PlyData.read(file_path)
        print(f"Elements: {list(plydata.elements)}")
        if 'vertex' in plydata:
            print(f"Vertex count: {plydata['vertex'].count}")
            print(f"Vertex properties: {plydata['vertex'].data.dtype.names}")
        return True
    except ImportError:
        print("plyfile not installed.")
        return False
    except Exception as e:
        print(f"Error reading with plyfile: {e}")
        return False

def read_with_trimesh(file_path):
    try:
        import trimesh
        print("\n--- Reading with trimesh ---")
        mesh = trimesh.load(file_path)
        print(f"Vertices: {len(mesh.vertices)}")
        if hasattr(mesh, 'faces'):
            print(f"Faces: {len(mesh.faces)}")
        return True
    except ImportError:
        print("trimesh not installed.")
        return False
    except Exception as e:
        print(f"Error reading with trimesh: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        file_path = "/home/ajoy/saumya/cv/ModelNet-10/train/bathtub/bathtub_0001.ply"
    else:
        file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    print(f"Testing reading of: {file_path}")
    
    read_with_open3d(file_path)
    read_with_plyfile(file_path)
    read_with_trimesh(file_path)
