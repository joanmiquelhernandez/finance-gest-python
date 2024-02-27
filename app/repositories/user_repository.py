from app import logger
from app.models import Base
from app.models.user import User
from app.repositories import session
from app.repositories.generic_crud_repository import GenericCrud

log_error = logger.setup_logger(f'{__name__}_error', 'error.log')
log_info = logger.setup_logger(f'{__name__}_info', 'info.log')

class UserRepo(GenericCrud):
    def get_by_email(self, email: str) -> User | None:
        """Obtiene Usuario por email

        Args:
            email (str): Email del usuario

        Returns:
            User | None: Usuario encontrado o None
        """
        try:
            return session.query(User).filter(User.email == email).one_or_none()
        except Exception as e:
            log_error.error(e)