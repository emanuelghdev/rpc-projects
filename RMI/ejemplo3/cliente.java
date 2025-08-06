import java.rmi.registry.LocateRegistry;
import java.rmi.*;
import java.rmi.registry.Registry;

public class cliente {
	public static void main(String[] args) {		
		try {
			// Creamos el stub para el cliente especificando el nombre del servidor
			Registry mireg = LocateRegistry.getRegistry("127.0.0.1", 1098);
			icontador micontador = (icontador)mireg.lookup("mmicontador");
			
			// Ponemos el contador al valor inicial 0
			System.out.println("Poniendo contador a 0");
			micontador.sumar(0);
			
			// Obtenemos hora de comienzo
			long horacomienzo = System.currentTimeMillis();
			
			// Incrementamos 1000 veces
			System.out.println("Incrementando...");
			for (int i = 0; i < 1000; i++ ) {
				micontador.incrementar();
			}
			
			// Obtenemos hora final, realizamos e imprimimos cálculos
			long horafin = System.currentTimeMillis();
			System.out.println("Media de las RMI realizadas = " + ((horafin - horacomienzo)/1000f) + " msegs");
			System.out.println("RMI realizadas = " + micontador.sumar());
		} catch(NotBoundException | RemoteException e) {
			System.err.println("Exception del sistema: " + e);
		}
		System.exit(0);
	}
}
