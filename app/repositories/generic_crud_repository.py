from typing import Union
from app.repositories import session
from app.models import Base

class GenericCrud():
    """Clase con los metodos basicos de CRUD, reusable para todas las clases

    Ejemplo:
        class User(GenericCrud):
         # Esta clase ya tiene los metodos Crud Basicos
    """

    def create(model_instance: Base) -> Base:
        """Guarda la instancia en BD

        Args:
            model_instance (Base): Objeto a guardar en Base de datos

        Returns:
            Base: Objeto actualizado con la info guardada en BD
        """
        session.add(model_instance)
        session.commit()
        session.refresh(model_instance)
        return model_instance

    def get_by_id(model_class: Base, id: int) -> Union[Base,None]:
        """Busca en BD el registro de la clase indicada que coincida con la id

        Args:
            model_class (Base): Clase de la que queremos buscar
            id (int): Identificador del registro

        Returns:
            Base: Registro encontrado o None
        """
        return session.query(model_class).filter_by(id=id).first_or_none()

    def update(model_instance: Base) -> Base:
        """Actualiza el registro de BD

        Args:
            model_instance (Base): Objeto actualizado con las nuevas propiedades

        Returns:
            Base: Objeto actualizado con la info guardada en BD
        """
        session.commit()
        session.refresh(model_instance)
        return model_instance

    def delete(model_instance: Base):
        """Elimina un registro de BD

        Args:
            model_instance (Base): Objeto que queremos eliminar el registro
        """
        session.delete(model_instance)
        session.commit()
