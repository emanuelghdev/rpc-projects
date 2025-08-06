import java.io.Serializable;

public class Donacion implements Serializable {
    private Entidad entidad;
    private double monto;

    public Donacion(Entidad entidad, double monto) {
        this.entidad = entidad;
        this.monto = monto;
    }

    public Entidad getEntidad() {
        return entidad;
    }

    public double getMonto() {
        return monto;
    }
}
