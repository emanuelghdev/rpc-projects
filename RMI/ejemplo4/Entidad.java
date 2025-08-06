import java.io.Serializable;
import java.util.Objects;

public class Entidad implements Serializable {
    private String nombre;

    public Entidad(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Entidad entidad = (Entidad) o;
        return Objects.equals(nombre, entidad.nombre);
    }

    @Override
    public int hashCode() {
        return Objects.hash(nombre);
    }
}
