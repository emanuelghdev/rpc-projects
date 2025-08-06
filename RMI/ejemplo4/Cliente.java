import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.List;

public class Cliente {
    public static void main(String[] args) {
        try {
            // Obtenemos la referencia al registro RMI en el localhost y puertos 1097 y 1098
            Registry registry1 = LocateRegistry.getRegistry("localhost", 1097);
            Registry registry2 = LocateRegistry.getRegistry("localhost", 1098);

            // Obtenemos la referencias a los servidores
            Donacion_I servidor1 = (Donacion_I) registry1.lookup("Servidor1");
            Donacion_I servidor2 = (Donacion_I) registry2.lookup("Servidor2");

            // Ejemplo de llamadas a métodos del servidor1
            Entidad entidad1 = new Entidad("Entidad1");
            servidor1.registrarEntidad(entidad1);
            servidor1.realizarDonacion(new Donacion(entidad1, 100.0));

            // Ejemplo de llamadas a métodos del servidor2
            Entidad entidad2 = new Entidad("Entidad2");
            Entidad entidad3 = new Entidad("Entidad3");
            Entidad entidad4 = new Entidad("Entidad4");
            servidor2.registrarEntidad(entidad2);
            servidor2.registrarEntidad(entidad3);
            servidor2.registrarEntidad(entidad4);
            servidor2.realizarDonacion(new Donacion(entidad2, 35.0));
            servidor2.realizarDonacion(new Donacion(entidad3, 100.0));
            servidor2.realizarDonacion(new Donacion(entidad4, 60.0));

            // Mostramos el total donado 
            System.out.println("\nTotal donado: " + servidor1.consultarTotalDonado());
            
            // Ejemplo de lista de donantes
            List<Entidad> donantes = servidor1.listarDonantes();
            System.out.println("\nLista de donantes: ");
            for (Entidad donante : donantes) {
                 System.out.println(donante.getNombre());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
