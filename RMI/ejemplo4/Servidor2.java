import java.rmi.*;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.ArrayList;
import java.util.List;

public class Servidor2 extends UnicastRemoteObject implements Donacion_I {
    private List<Entidad> entidadesRegistradas;
    private double subtotalDonado;
    private int numEntidades;
    private Donacion_I replica;

    public Servidor2() throws RemoteException {
        entidadesRegistradas = new ArrayList<>();
        subtotalDonado = 0.0;
        numEntidades = 0;
        replica = null;
    }

    @Override
    public synchronized void registrarEntidad(Entidad entidad) throws RemoteException {
    	replica = this.getReplica();
    	
        if (!entidadesRegistradas.contains(entidad) && replica.getNumEntidades() >= numEntidades) {
            entidadesRegistradas.add(entidad);
            numEntidades++;
            System.out.println("Entidad registrada en Servidor2: " + entidad.getNombre());
        }
        else if(!entidadesRegistradas.contains(entidad)){
        	replica.registrarEntidad(entidad);
        }
    }

    @Override
    public synchronized void realizarDonacion(Donacion donacion) throws RemoteException {
        if (entidadesRegistradas.contains(donacion.getEntidad())) {
            subtotalDonado += donacion.getMonto();
            System.out.println("Donación de " + donacion.getMonto() + "€, realizada en Servidor2 por " + donacion.getEntidad().getNombre());
        }
        else if (replica.listarDonantes().contains(donacion.getEntidad())){
        	replica.realizarDonacion(donacion);
        }
    }

    @Override
    public synchronized double consultarSubTotalDonado() throws RemoteException {
        return subtotalDonado;
    }
    
    @Override
    public synchronized double consultarTotalDonado() throws RemoteException {
        return subtotalDonado + replica.consultarSubTotalDonado();
    }
    
    @Override
    public int getNumEntidades() throws RemoteException {
        return numEntidades;
    }
    
    @Override
    public List<Entidad> listarParcialDonantes() throws RemoteException {
        return entidadesRegistradas;
    }

    @Override
    public synchronized List<Entidad> listarDonantes() throws RemoteException {
    	List<Entidad> entidadesTotales = new ArrayList<>();
    	entidadesTotales.addAll(entidadesRegistradas);
    	entidadesTotales.addAll(replica.listarParcialDonantes());
    	
        return entidadesTotales;
    }
    
    public synchronized Donacion_I getReplica() throws RemoteException {
        try {
		    Registry registry = LocateRegistry.getRegistry(1097);
		    return (Donacion_I) registry.lookup("Servidor1");
		} catch (NotBoundException | RemoteException e) {
		    e.printStackTrace();
		    throw new RemoteException("Error al obtener la réplica del servidor.", e);
		}
    }

    public static void main(String[] args) {
        try {
            // Creamos e inicializamos el registro RMI
            Registry registry = LocateRegistry.createRegistry(1098);

            // Creamos una instancia del servidor2 y vinculamos al registro
            Servidor2 servidor2 = new Servidor2();
            registry.rebind("Servidor2", servidor2);

            System.out.println("Servidor2 listo...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
