import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
//import contador.contador;

public class servidor {
	public static void main(String[] args) {
		try {
			// Creamos una instancia de contador
			// System.setProperty("java.rmi.server.hostname","127.0.0.1");
			Registry reg=LocateRegistry.createRegistry(1098);
			contador micontador = new contador();
			reg.rebind("mmicontador", micontador);
			// suma = 0;
			System.out.println("Servidor preparado");
		} catch (RemoteException e) {
			System.out.println("Exception: " + e.getMessage());
		}
	}
}
