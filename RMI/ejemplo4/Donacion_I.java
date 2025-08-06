import java.rmi.*;
import java.util.List;

public interface Donacion_I extends Remote {
    void registrarEntidad(Entidad entidad) throws RemoteException;
    void realizarDonacion(Donacion donacion) throws RemoteException;
    double consultarSubTotalDonado() throws RemoteException;
    double consultarTotalDonado() throws RemoteException;
    int getNumEntidades() throws RemoteException;
    List<Entidad> listarParcialDonantes() throws RemoteException;
    List<Entidad> listarDonantes() throws RemoteException;
    Donacion_I getReplica() throws RemoteException;
}
